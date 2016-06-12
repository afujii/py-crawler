//
// init
// ----------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', init)

function init() {
    const route = window.location.pathname

    if (!/\/$|\/login$/.test(route) && !window.sessionStorage.getItem('auth_key')) {
        window.location.pathname = '/'
        return false
    }

    switch (route) {
        case '/in-theaters':
            initInTheaters()
            break
        case '/coming-soon':
            initComingSoon()
            break
        case '/rank':
            initRank()
            break
        default:
            initLogin()
    }
}

//
// in theaters page
// ----------------------------------------------------------------------------
function initInTheaters() {
    $('a[href="/in-theaters"]').addClass('active')
    console.log('in-theaters inited')
}



//
// coming soon page
// ----------------------------------------------------------------------------
function initComingSoon() {
    $('a[href="/coming-soon"]').addClass('active')
    console.log('coming-soon inited')
}



//
// rank page
// ----------------------------------------------------------------------------
function initRank() {
    $('a[href="/rank"]').addClass('active')
    $('.genre').on('click', onSelectGenre)

    console.log('rank inited')
}

function onSelectGenre() {
    window.location.search = '?sort=' + $(this).text()
}

//
// login page
// ----------------------------------------------------------------------------
function initLogin() {
    $('a[href="/login"]').addClass('active')
    $('#btn-login').on('click', onLogin)
    $('#btn-register').on('click', onRegister)
    console.log('login inited')
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
        $.post('/api/login', { username, password }, res => {
            const parsed = JSON.parse(res)
            parsed.status === 200 ? resolve(parsed) : reject(parsed)
        })
    })

    req.then(res => {
        console.log('login succeed', res)
        window.sessionStorage.setItem('auth_key', res.data.auth_key)
        window.alert('登录成功')
        window.location.href = '/in-theaters'
        return false
    }).catch(err => {
        console.error('login faild', err)
        window.sessionStorage.removeItem('auth_key')
        window.alert('登录失败')
        return false
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
        $.post('/api/register', { username, password }, res => {
            const parsed = JSON.parse(res)
            parsed.status === 200 ? resolve(parsed) : reject(parsed)
        })
    })

    req.then(res => {
        console.log('register succeed', res)
        window.alert('注册成功')
        return false
    }).catch(err => {
        console.error('register faild', err)
        window.alert('注册失败')
        return false
    })
}

//
// utils
// ----------------------------------------------------------------------------
function modal() {
    $('#model').modal()
}
