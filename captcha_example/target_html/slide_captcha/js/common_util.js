/***
 * 返回鼠标的坐标
 * @param e
 * @returns {{x: (Number|pageX|*), y: (Number|pageY|*)}}
 */
 var getCoordInDocument = function(e) {
    e = e || window.event;
    var x = e.pageX || (e.clientX +
        (document.documentElement.scrollLeft
            || document.body.scrollLeft));
    var y= e.pageY || (e.clientY +
        (document.documentElement.scrollTop
            || document.body.scrollTop));
    return {'x':x,'y':y};
}