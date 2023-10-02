var loadBtn =document.getElementById("load-articles");
var articleContainer = document.getElementById("articles");
loadBtn.addEventListener( "click" , function() {
    axios.get("/all-articles/").then(function(a) {
        articleContainer.innerHTML=a.data;
    }).catch(function (err) {
        console.log(err);        
    });
});

var form =document.getElementById("form");
form.addEventListener("submit",function(event){
    event.preventDefault();
    var fd = new FormData();
    fd.append("title",document.getElementById("title").value);
    fd.append("desciption",document.getElementById("desciption").value);
    fd.append('csrfmiddlewaretoken','{{csrf_token}}')
    axios.post("/create-article/",fd)
    .then(function(resp){
        if(resp.data.status === "success"){
           loadBtn.click();
           form.reset(); 
        }       
    }).catch(function(err){
        console.log(err);
    });
});
