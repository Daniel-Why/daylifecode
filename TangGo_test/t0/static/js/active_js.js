console.log("active_js.js load success");

// 直接定义postRequest函数
function postRequest() {
    const params = new URLSearchParams();
    params.append('p1', 'John');
    params.append('p2', '23');

    fetch('http://192.168.3.130:999/post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: params.toString(),
        mode: 'cors',
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.text();
    })
    .then(data => {
        console.log('Success:', data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
};