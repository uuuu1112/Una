const navSlide=()=>{
    const burger = document.querySelector('.burger')
    const sidebarMenu=document.querySelector('.sidebarMenu')

    burger.addEventListener('click',()=>{
        sidebarMenu.classList.toggle('sidebarMenu-active')
    });
}

navSlide();