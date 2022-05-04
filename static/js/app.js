const initFooter=()=>{
    
}
const navSlide=()=>{
    const menu = document.querySelector('.menu')
    const sidebar=document.querySelector('.sidebar')
    const clear=document.querySelector('.clear')
    const mask=document.querySelector('.mask')
    const body=document.body

    menu.addEventListener('click',()=>{
        sidebar.classList.toggle('sidebar-active')
        mask.style.display='block';
        body.style.overflowY='hidden';
    });
    clear.addEventListener('click',()=>{
        sidebar.classList.toggle('sidebar-active')
        mask.style.display='none';
        body.style.overflow='auto';
    });
}

navSlide();