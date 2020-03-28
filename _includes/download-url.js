function getOS() {
  // Supports and returns one of: Windows, macOS, Linux, Android, iOS, or null if unknown
  const userAgent = window.navigator.userAgent;
  const platform = window.navigator.platform;

  const macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K"];
  const windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"];
  const iosPlatforms = ["iPhone", "iPad", "iPod"];

  if (macosPlatforms.indexOf(platform) !== -1) {
    return "macOS";
  } else if (iosPlatforms.indexOf(platform) !== -1) {
    return "iOS";
  } else if (windowsPlatforms.indexOf(platform) !== -1) {
    return "Windows";
  } else if (/Android/.test(userAgent)) {
    return "Android";
  } else if (/Linux/.test(platform)) {
    return "Linux";
  } else {
    // Unknown
    return null;
  }
}

function getDownloadInfo() {
  let os = getOS();
  if (os !== null) {
    let version = "{{ site.data.downloads.version }}";
    let platforms = JSON.parse(`{{ site.data.downloads.platforms | jsonify }}`);
    let p = platforms.filter((p) => p.name === os)[0] || null;
    if (p !== null) {
      return {
        title: `${p.name}, ${p.assets[0].title}, ${version}`,
        url: p.assets[0].url,
      };
    }
  }

  // If all else fails
  return {
    title: "All platforms",
    url: `/downloads/`,
  };
}

function adaptDownloadButton() {
  let downloadinfo = getDownloadInfo();
  console.log(downloadinfo);

  let $button = document.getElementById("download");
  $button.href = downloadinfo.url;

  let $info = document.getElementById("download-info");
  $info.innerHTML = downloadinfo.title;

  console.log(`Set {downloadinfo}`);
}
