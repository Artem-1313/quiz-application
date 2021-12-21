 document.addEventListener("DOMContentLoaded", () => {

    var url = window.location.origin
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
	var data = {}
	data['csrfmiddlewaretoken'] = csrf[0].value
	var quiz_form = document.getElementById('quiz-form');
	var elem = [...document.getElementsByClassName('ans')];

	const sendData = () =>{
	elem.forEach(el => {

    if (!data[el.name]) {
        data[el.name]=[null]
      if (el.checked){

        data[el.name] = [el.value]
      }
    } else {
      if (el.checked){

      data[el.name].push(el.value)

      }
    }
console.log(data)
	})

	$.ajax({
	 type:'POST',
	 url: `${url}/quiz/test/`,
	 data: data,
	 success:function (response){
	 console.log(data)
	    quiz_form.style.display = 'none'
	 //
        response.test.forEach(res =>{
        for (const [question, answer] of Object.entries(res)) {
          var finalDiv = document.createElement("div")
          finalDiv.classList.add("container", "finalDiv")
           finalDiv.innerHTML+=`<h3>${question}</h3>`;

         if (answer['is_right'] == 1){

            finalDiv.classList.add("correct_ans")
            finalDiv.innerHTML+=`Ваша відповідь правильна= <b>${answer['answer']}</b>`
         }
         if (answer['is_right'] == 0){

            finalDiv.classList.add("not-ans")

            finalDiv.innerHTML+=` Ваша відповідь НЕПРАВИЛЬНА= <b>${answer['answer']}</b>
            <p>Правильна відповідь= <b>${answer['correct_ans']}</b></p>`
         }
          if (answer['not_answer'] == 1){
          finalDiv.classList.add("not-ans")
          finalDiv.innerHTML+=` Ви не дали відповідь!  <p>Правильна відповідь= <b>${answer['correct_ans']}</b></p>`

         }
        var body = document.getElementsByTagName('body')[0]
        body.append(finalDiv)
        }// end dict loop Object.entries(res)

        })// end response.test loop

//console.log(response.test)

//
	 },
	 error: function (err){console.log(err)}

	})
}
	quiz_form.addEventListener('submit', e =>{
	e.preventDefault()

	sendData()
	})
 });