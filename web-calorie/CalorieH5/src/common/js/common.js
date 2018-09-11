// document.getElementsByTagName('title')[0].innerHTML = val;
// window.setDocumentTitle = function(title) {
//   var i = document.createElement('iframe');
//   i.src = '../favicon.ico';
//   i.style.display = 'none';
//   i.onload = function() {
//     setTimeout(function(){
//       i.remove();
//     }, 9)
//   }
//   document.body.appendChild(i);
// };//ios
const common = {
  changeTitle:function (val){
    document.getElementsByTagName('title')[0].innerHTML = val;
    window.setDocumentTitle = function(title) {
      var i = document.createElement('iframe');
      i.src = '../favicon.ico';
      i.style.display = 'none';
      i.onload = function() {
        setTimeout(function(){
          i.remove();
        }, 9)
      }
      document.body.appendChild(i);
    };//ios
  },
  GetQueryString(name) {
    var url = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
    var newUrl = window.location.search.substr(1).match(url);
    if (newUrl != null) {
      return unescape(newUrl[2]);
    } else {
      return false;
    }
  },
  getScrollTop() {
    var scrollTop = 0;
    if (document.documentElement && document.documentElement.scrollTop) {
      scrollTop = document.documentElement.scrollTop;
    } else if (document.body) {
      scrollTop = document.body.scrollTop;
    }
    return scrollTop;
  },
}
export default common
