function isValid(date, h1, m1, h2, m2) {
  var h = date.getHours();
  var m = date.getMinutes();
  return (h1 < h || h1 == h && m1 <= m) && (h < h2 || h == h2 && m <= m2);
}

setInterval(() => {
idk2()
},2000)
function idk2() {
f = new Date()

if (f.getDay() != 6 && f.getDay() != 0) {
if (isValid(f, 7, 55, 10, 51) || isValid(f, 11, 26, 15, 0)) {
window.location = '/'
};
}

}
idk2()