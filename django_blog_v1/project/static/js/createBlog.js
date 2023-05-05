headerName = 2
textAreaName = 2
ImageName = 2
document.getElementById("addHeader").addEventListener("click", addHeader);
document.getElementById("addText").addEventListener("click", addText);
document.getElementById("addImage").addEventListener("click", addImage);
document.getElementById("sendBlog").addEventListener("click", sendBlog);


function addHeader() {
  
  const blogElements = document.getElementById("blogElements");
  const header = document.createElement("input");
  header.classList.add("mb-3");
  header.classList.add("form-control");
  header.classList.add("form-control-lg");
  headerName = headerName+ 1
  console.log(headerName)
  header.name = "header"+headerName.toString();
  console.log(headerName)
  header.type = "text";
  blogElements.appendChild(header);

}

function addText() {
    const blogElements = document.getElementById("blogElements");
    const Textarea = document.createElement("textarea");
    Textarea.classList.add("form-control");
    Textarea.classList.add("mb-3");
    textAreaName = textAreaName+ 1
    Textarea.name = "textArea"+textAreaName.toString();
    blogElements.appendChild(Textarea);
}
  
function addImage() {
const blogElements = document.getElementById("blogElements");
  const fileInput = document.createElement("input");
  fileInput.classList.add("mb-3");
  fileInput.classList.add("form-control");
  fileInput.type = "file";
  fileInput.accept = "image/png, image/jpeg"
  ImageName = ImageName +1
  fileInput.name = "ImageName"+ImageName.toString();
  
  blogElements.appendChild(fileInput);

}

function sendBlog()
{
    console.log("burda")
    const blogElements = document.getElementById("blogElements");
    
}