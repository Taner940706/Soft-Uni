function solve() {
    document.getElementById("publish-btn").addEventListener("click", publishPost);
    
  
    let title = document.getElementById("post-title");
    let category = document.getElementById("post-category");
    let contents = document.getElementById("post-content");
  
    function publishPost(){
      let ul = document.getElementById("review-list");
      
      if (title.value != "" && category.value != "" && contents.value != ""){
  
        let li = document.createElement("li");
        let h4 = document.createElement("h4");
        let p1 = document.createElement("p");
        let p2 = document.createElement("p");
        let article = document.createElement("article");
        let btn_1 =  document.createElement("button");
        let btn_2 =  document.createElement("button");
        li.classList.add("rpost");
        btn_1.classList.add("action-btn","edit");
        btn_2.classList.add("action-btn","approve");
  
        h4.textContent = title.value;
        p1.textContent = "Category: "+category.value;
        p2.textContent = "Content: "+contents.value;
        btn_1.textContent = "Edit";
        btn_2.textContent = "Approve";
  
        article.appendChild(h4);
        article.appendChild(p1);
        article.appendChild(p2);
        li.appendChild(article);
        li.appendChild(btn_1);
        li.appendChild(btn_2);
  
        ul.appendChild(li)
  
        title.value = "";
        category.value = "";
        contents.value = "";
  
  
      }
  
      let x = document.querySelectorAll('[class*="edit"]')[0];
      let y = document.querySelectorAll('[class*="approve"]')[0];
      document.getElementById("clear-btn").addEventListener("click", clearPost);
      x.addEventListener("click", editPost);
      y.addEventListener("click", ApprovePost);
  
      function editPost(){
        let h4_post = document.getElementsByTagName('article')[0].children[0].textContent;
        let p1_post = document.getElementsByTagName('article')[0].children[1].textContent;
        let p2_post = document.getElementsByTagName('article')[0].children[2].textContent;
    
        title.value = h4_post;
        category.value = p1_post.replace('Category: ','');;
        contents.value = p2_post.replace('Content: ','');;
    
        document.getElementsByClassName("rpost")[0].remove();
    
      }
  
      function ApprovePost(){
        const node = document.getElementsByClassName("rpost")[0];
        const clone = node.cloneNode(true);
        document.getElementById("published-list").appendChild(clone);
        document.getElementsByClassName("rpost")[0].remove();
        document.querySelectorAll('[class*="edit"]')[0].remove();
        document.querySelectorAll('[class*="approve"]')[0].remove();
  
  
      }
  
      function clearPost(){
        document.getElementsByClassName("rpost")[0].remove();
  
      }
  
  
  
  
    }
  
    
  }