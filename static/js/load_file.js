const dropZone = document.querySelector('div')
const input = document.body.querySelector('input')
let file


document.addEventListener('dragover', ev => ev.preventDefault())
document.addEventListener('drop', ev => ev.preventDefault())
dropZone.addEventListener('drop', event => {
    event.preventDefault()
    file = event.dataTransfer.files[0]
    /*
    File {name: "image.png", lastModified: 1593246425244, lastModifiedDate: Sat Jun 27 2020 13:27:05 GMT+0500 (Екатеринбург, стандартное время), webkitRelativePath: "", size: 208474, …}
        lastModified: 1593246425244
        lastModifiedDate: Sat Jun 27 2020 13:27:05 GMT+0500 (Екатеринбург, стандартное время) {}
        name: "image.png"
        size: 208474
        type: "image/png"
        webkitRelativePath: ""
        __proto__: File
    */

    //передаем файл в функцию для дальнейшей обработки
    handleFile(file)
})
const handleFile = file => {    
    const data_type = file.type.replace(/\/.+/, '')
    const file_type = file.name.split('.')[1]
    const file_name = file.name.split('.')[0]

    //let reader = new FileReader()
    //reader.readAsArrayBuffer(file)
    //reader.onload = function() {
      //  console.log(reader.result)
    //}
    responseFile(file)
    //let response = fetch("http://127.0.0.1:5000/load_file", {
      //  method: 'POST',
        //body: read_file
      //});
    //console.log(`Имя: "${file_name}"\nТип файла: "${data_type}"\nРасширение: "${file_type}"`)
function responseFile(file) { 
  const data = new FormData(); 
  data.append('file', file) 
  console.log(data)
  return fetch('http://127.0.0.1:5000/load_file/', {method: 'post', body: data}).catch(console.error)}
}