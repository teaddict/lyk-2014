

<!--1 -->
<p id="demo">my first paragraph</p>
<p id="obje"></p>
<p id="phone"></p>
<p id="phone1"></p>
<p id="phone2"></p>
<p id="func"></p>
<script>
document.getElementById("demo").innerHTML="My first JavaScript";

<!--obje bilgilerini yazdırma -->
var person={firstname:"Fatih",lastname:"Metin"};
document.getElementById("obje").innerHTML=person.firstname +" "+ person.lastname;

<!-- mapping veri yapısı, data çağırma -->
var phone={"Ali":"5554446622",
		   "Veli":"5364789654",
           "Cem": "5232455654",
            1:	  "text122334",
            "x": ["ali",2,3]};

document.getElementById("phone").innerHTML=phone["Cem"];
document.getElementById("phone1").innerHTML=phone[1];
document.getElementById("phone1").innerHTML=phone["x"];

<!-- cemin tel no istedik burda "isim"-> key -->


<!--fonksiyon tanımı -->
function myname(name)
{
console.log(name); <!-- log olarak yazdırır -->
console.log("Hi" + name);
}
<!-- function return a value -->
function add(x,y)
{
return x+y;
}

document.getElementById("func").innerHTML="toplam: "+ add(2,3);


</script>
