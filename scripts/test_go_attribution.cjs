// Offline execution of the real redirect and subscribe scripts. No network.
// Run: node --test scripts/test_go_attribution.cjs
const assert = require('node:assert/strict');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { test } = require('node:test');
const vm = require('node:vm');

const root = join(__dirname, '..');
function scriptFrom(file, marker) {
  const html = readFileSync(join(root, file), 'utf8');
  const script = [...html.matchAll(/<script(?:\s[^>]*)?>([\s\S]*?)<\/script>/g)]
    .map(match => match[1]).find(code => code.includes(marker));
  assert.ok(script, `Missing script in ${file}`);
  return script;
}
const redirect = scriptFrom('go/index.html', 'var SRC_DEFAULT');
const subscribe = scriptFrom('subscribe.md', 'DOMContentLoaded');

function go(search) {
  const result = { events: [], navigations: [], fallback: null };
  const timers = [];
  vm.runInNewContext(redirect, {
    URLSearchParams, encodeURIComponent,
    window: { location: { search, replace: url => result.navigations.push(url) } },
    document: { getElementById: () => ({ setAttribute: (_, url) => { result.fallback = url; } }) },
    setTimeout: callback => timers.push(callback),
    gtag: (_, event, options) => {
      result.events.push({ event, src: options.src, dest: options.dest });
      options.event_callback();
    },
  });
  timers.forEach(callback => callback());
  assert.equal(result.navigations.length, 1, 'Tracker callback plus timeout must navigate once');
  assert.equal(result.fallback, result.navigations[0]);
  return result;
}

function checkoutLinks(firstHop) {
  const page = readFileSync(join(root, 'subscribe.md'), 'utf8');
  const links = [...page.matchAll(/href="(\/go\/[^\"]+)"/g)]
    .map(match => ({ href: match[1].replaceAll('&amp;', '&') }));
  assert.equal(links.length, 5);
  const url = new URL(firstHop);
  vm.runInNewContext(subscribe, {
    URLSearchParams, URL, encodeURIComponent,
    window: { location: { search: url.search, origin: url.origin } },
    document: {
      referrer: '',
      addEventListener: (event, callback) => { assert.equal(event, 'DOMContentLoaded'); callback(); },
      querySelectorAll: () => links,
    },
  });
  return links.map(link => new URL(link.href, url.origin));
}

for (const tag of ['forum-release-v014', 'reddit-release-v014', 'linkedin-release-v014', 'webext']) {
  test(`${tag}: redirect -> real subscribe links -> all five Stripe plans`, () => {
    const first = go('?src=' + tag);
    assert.deepEqual(first.events, [{ event: 'nudge_click', src: tag, dest: 'subscribe' }]);
    assert.equal(first.navigations[0], 'https://activitywatch.net/subscribe?from=' + tag);
    for (const link of checkoutLinks(first.navigations[0])) {
      assert.equal(link.searchParams.get('from'), tag);
      const second = go(link.search);
      const stripe = new URL(second.navigations[0]);
      assert.equal(stripe.origin, 'https://buy.stripe.com');
      assert.equal(stripe.searchParams.get('client_reference_id'), tag);
      assert.equal(second.events[0].src, 'web-subscribe');
    }
  });
}

test('unknown source and origin remain outside the allowlist', () => {
  const first = go('?src=unregistered-release-v014');
  assert.equal(first.events[0].src, 'other');
  assert.equal(first.navigations[0], 'https://activitywatch.net/subscribe?from=other');
  const second = go('?src=web-subscribe&to=stripe-personal-monthly&from=unregistered-release-v014');
  assert.equal(new URL(second.navigations[0]).searchParams.get('client_reference_id'), 'web-subscribe');
});

test('raw URL destination is rejected even with a registered channel', () => {
  const result = go('?src=forum-release-v014&to=' + encodeURIComponent('https://evil.example/checkout'));
  assert.equal(result.navigations[0], 'https://activitywatch.net/subscribe?from=forum-release-v014');
});

test('existing forum source still routes to the community forum', () => {
  assert.equal(go('?src=forum').navigations[0], 'https://forum.activitywatch.net');
});
