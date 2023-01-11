// Invoke Functions Call on Document Loaded

var messageWrapper = document.querySelector('.alert')
console.log(messageWrapper)
setTimeout(function(){
  messageWrapper.style.display = 'none';
}, 5000)