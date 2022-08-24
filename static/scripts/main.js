const nav = document.querySelector('.navigation')
const menu = document.querySelector('.navigation>.nav>ul')
const arrow = document.querySelector('.arrow')
const arrow_svg = document.querySelector('.arrow>svg')
const arrow_path = document.querySelector('.arrow>svg>path')
const parent_box = document.querySelector('.parent')


let flag = 0
nav.style.transform = `translateY(-${menu.offsetHeight+10}px)`
window.addEventListener('resize', function(){
    let flag = 0
    taskbox.style.marginTop = nav.offsetHeight+20+'px'
    nav.style.transform = `translateY(-${menu.offsetHeight+10}px)`
})

arrow.addEventListener('click', function(){
    if(flag === 0){
        nav.style.transform = 'translateY(0)'
        arrow_svg.style.transform = 'rotateX(180deg)'
        flag = 1
    }
    else{
        nav.style.transform = `translateY(-${menu.offsetHeight+10}px)`
        arrow_svg.style.transform = 'rotateX(0deg)'
        flag = 0
    }
})