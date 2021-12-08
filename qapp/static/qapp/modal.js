document.addEventListener('DOMContentLoaded', ()=>{

var modalBtns = [...document.getElementsByClassName('btn-modal')]
var modalBody = document.getElementById('modal-body')
var startQuiz = document.getElementById('start-quiz')
modalBtns.forEach( modalBtn => {
	modalBtn.addEventListener('click', function (){
	const id = modalBtn.getAttribute('data-id');
	const name = modalBtn.getAttribute('data-quiz');
	const description = modalBtn.getAttribute('data-description');
	modalBody.innerHTML=`
	<p>Тест з ${name}</p>
	<p>Опис ${description}</p>

	`
	startQuiz.onclick = ()=>{
		window.location.href+=id
	}
})

})

})

