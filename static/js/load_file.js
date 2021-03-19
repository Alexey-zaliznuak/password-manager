const dropZone = document.querySelector('div')
const input = document.body.querySelector('input')
const UID = document.querySelector('.input').id
let file

document.addEventListener('dragover', ev => ev.preventDefault())
document.addEventListener('drop', ev => ev.preventDefault())
dropZone.addEventListener('drop', event => {
    event.preventDefault()
    file = event.dataTransfer.files[0]
    handleFile(file)
})

const handleFile = file => {    
    const data_type = file.type.replace(/\/.+/, '')
    const file_type = file.name.split('.')[1]
    const file_name = file.name.split('.')[0]
    responseFile(file)

function responseFile(file) { 
  const data = new FormData(); 
  data.append('file', file) 
  console.log(data)
  return fetch(`http://127.0.0.1:5000/load_file?UID=${UID}`, {method: 'post', body: data}).catch(console.error)}
}