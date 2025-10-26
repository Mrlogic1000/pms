sidebar = document.getElementById('nav')  
btn = document.getElementById('btn')  
modal_layer = document.getElementById('modal-layer')
modal_close = document.getElementById('modal-close')
modal_open = document.getElementById('modal-open')

modal_close.addEventListener('click',function(){
    modal_layer.style.display = 'none'

})
modal_open.addEventListener('click',function(){
    modal_layer.style.display = 'block'

})

