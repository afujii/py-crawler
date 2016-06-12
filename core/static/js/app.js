document.addEventListener('DOMContentLoaded', init)

function init() {
    $('#btn-login').on('click', onLogin);
    $('#btn-register').on('click', onRegister);
    console.log('app inited')
}

function onLogin() {
    console.log('start login')

    const username = $('#login-username').val()
    const password = $('#login-password').val()

    if (username.length < 1) {
        window.alert('用户名不合法')
        return false
    }

    if (password.length < 6) {
        window.alert('请输入至少6位的密码')
        return false
    }

    const req = new Promise((resolve, reject) => {
        $.post('/api/login', { username, password }, resolve)
    })

    req.then(res => {
        console.log('login succeed', res)
    })
}

function onRegister() {
    console.log('start register')

    const username = $('#register-username').val()
    const password = $('#register-password').val()
    const repeat = $('#register-repeat').val()

    if (username.length < 1) {
        window.alert('用户名不合法')
        return false
    }

    if (password.length < 6) {
        window.alert('请输入至少6位的密码')
        return false
    }

    if (password !== repeat) {
        window.alert('两次密码不匹配')
        return false
    }

    const req = new Promise((resolve, reject) => {
        $.post('/api/register', { username, password }, resolve)
    })

    req.then(res => {
        console.log('register succeed', res)
    })
}
