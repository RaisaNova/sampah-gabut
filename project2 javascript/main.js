const body = document.body
const btn1 = document.getElementById('btn1') 
const btn2 = document.getElementById('btn2')

const defaultText = 'klik saya'
btn1.textContent = defaultText

btn1.style.broder = 'none'
btn1.style.padding = '8px'
btn1.style.frontSize = '24px'
btn1.style.background = 'tomato'

function gantiWarna(){
    btn1.style.background = 'aqua'
}

function ubahText() {
    btn1.textContent = 'kasiddddddd'
}

function oriText(){
btn1.textContent = defaultText

}

function newText() {
 newText.textContent = "neta sabrina"
 body.append("neta Sabrina") 

}






