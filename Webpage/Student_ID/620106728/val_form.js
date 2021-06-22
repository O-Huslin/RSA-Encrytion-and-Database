/*const clerk = document.getElementById("c_id");
    const con_id = document.getElementById("con_id");
    const pd = document.getElementById("pd");
    const ps = document.getElementById("ps");
    const c1 = document.getElementById("c1");
    const c2 = document.getElementById("c2");
    const r = document.getElementById("r");
    const form = document.getElementById("fm");
    const errorElement = document.getElementById("e_msg");

form.addEventListener("submit", (e) => {
    let msg=[]
    if(clerk.value === "" || clerk.value == null){
        msg.push("Please check Clerk ID");
    }
    if(msg.length > 0){
        e.preventDefault()
        errorElement.innerText = msg.join(", ")
    }
    
})
*/
function vali_form(){

    let clerk = document.getElementById("c").value;
    let con_id = document.getElementById("ci").value;
    let pd = document.getElementById("pd").value;
    let ps = document.getElementById("ps").value;
    let c1 = document.getElementById("c1").value;
    let c2 = document.getElementById("c2").value;
    let r = document.getElementById("r").value;
    let total = document.getElementById("total").value;
    let form = document.getElementById("fm");
    let errorElement = document.getElementById("e_msg");
    let text = "Please check field of ";
    const tot = c1 + c2 + r;

    alert(clerk);
    alert(text);

    if(clerk === "" || clerk == null || typeof clerk !== "number"){
        text += "Clerk ID"
        alert(text)
    }/*
    if(con_id === "" || con_id == null || typeof con_id !== "number"){
        text += "Constituency ID and that it is a number";
        alert(text);
    }
    if(pd === "" || pd == null || typeof pd!== "number"){
        text += "Polling Division ID and that is a number";
        alert(text);
    }
    if(ps === "" || ps == null){
        text += "Polling Station ID";
        alert(text);
    }
    if(c1 === "" || c1 == null || typeof c1 !== "number"){
        text += "Candiate\'s 1 number of votes and that it is a number";
        alert(text);
    }
    if(c2 === "" || c2 == null || typeof c2 !== "number"){
        text += "Candiate\'s 2 number of votes and that it is a number";
        alert(text);
    }
    if(r === "" || r == null || typeof r !== "number"){
        text += "Rejected number of votes and that it is a number"
        alert(text);
    }
    if(tot !== total){
        text = "The total vote does not match the sum of the candidates and reject votes";
        alert(text);
    }*/
}
