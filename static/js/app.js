const navSlide=()=>{
    const burger = document.querySelector('.burger')
    const sidebarMenu=document.querySelector('.sidebarMenu')
    const clear=document.querySelector('.clear')

    burger.addEventListener('click',()=>{
        sidebarMenu.classList.toggle('sidebarMenu-active')
    });
    clear.addEventListener('click',()=>{
        sidebarMenu.classList.toggle('sidebarMenu-active')
    });
}

navSlide();