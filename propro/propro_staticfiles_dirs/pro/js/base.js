// $(document).ready(function(){
// 	var searchForm = $('#search-form')
// 	var searchInput = searchForm.find('[name="search"]')
// 	var searchButton = searchForm.find('[type="submit"]')
// 	var typingTimer;
// 	var typingInterval = 100

// 	searchForm.keyup(function(event){
// 		clearTimeout(typingTimer)
// 		typingTimer = setTimeout(searchAuto, typingInterval)
// 	})
// 	searchForm.keydown(function(event){
// 		clearTimeout(typingTimer)
// 	})
// 	function spinButton(){
// 		searchButton.addClass('disabled')
// 		searchButton.html('<i class="fa fa-spin fa-spinner"></i> Searching...')
// 	}
// 	function searchAuto(){
// 		spinButton()
// 		var inputVal = searchInput.val()
// 		window.location.href = 'project?search=' + inputVal
// 	}
// })