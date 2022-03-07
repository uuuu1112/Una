const navSlide=()=>{
    const menu = document.querySelector('.menu')
    const sidebar=document.querySelector('.sidebar')
    const clear=document.querySelector('.clear')

    menu.addEventListener('click',()=>{
        sidebar.classList.toggle('sidebar-active')
    });
    clear.addEventListener('click',()=>{
        sidebar.classList.toggle('sidebar-active')
    });
}

navSlide();