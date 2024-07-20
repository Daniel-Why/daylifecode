document.addEventListener("DOMContentLoaded", function() {
    var outputElement = document.getElementById("js0");
    outputElement.innerHTML = "载入的一个小飞机";
});

function myFunction() {
    document.getElementById("js1").innerHTML = "载入了一个飞行员JoJo";

    var scriptTag = document.createElement('script');
    scriptTag.src = '../../static/js/active_js.js'; // 确保这个路径与实际文件位置相符
    scriptTag.onload = function() {
        document.getElementById('sendRequest').addEventListener('click', postRequest);
    };
    document.head.appendChild(scriptTag);
}

