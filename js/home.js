//alert("Loaded");

var phoneBook={
	"Ali":"05543432",
	"Cem":"05231121",
	"Gül":"03124562"};
	
document.write("<h1>Test</h1>");

function sayHi(name)
{
	console.log(name)
	}
	
	function count(name)
{
	if(name.length)
	{
	console.log(name.length)
	}
	return "foo";
	}
	
	function sayHiArray(array)
	{
	for(var i=0; i<array.length; i++)
	{
	console.log(array[i].length);	
	};		
	/* foreach kullanımı */
	for(var i in array)
	{
		console.log(array[i].length)
	};
	console.log("\n");
	/* while kullanımı */
	var k=0;
	while(k<array.length)
	{
		console.log(array[k++].lenght);
		
		}
	
		
	}
	
	function changeColor(query)
	{
	var color=prompt('hangi renk?');
	while(!validate(color))
	{
		 color=prompt('hangi renk?');
	}
	var elements=document.querySelectorAll(query);
	elements=Array.prototype.slice.call(elements);
	for(var n in elements)
	{
		var e=elements[n];
		//debugger
		e.style.color=color;
	};
	}
	
	//changeColor("h2");
	
	function validate(color)
	{
	var renk={"red":true,"blue":true,"yellow":true,"green":true}; //OBJE OLARAK
	if(renk[color])
	return true;
	else
	return false;
	}
	
	function validate2(color)
	{
	var renk=["red","blue","yellow","green"]; //ARRAY OLARAK
	for(var i in renk)
	{
	
	var validColor=renk[i];
	if(color==validColor)
	return true;
	
	}
	return false;
   } 
   
   
   function changeColorInput()
	{
	var renk=document.getElementById("colorInput");	
	var elements=document.querySelectorAll(".sub-title");
	elements=Array.prototype.slice.call(elements);
	for(var n in elements)
	{
		var e=elements[n];
		//debugger
		e.style.color=renk.value; //
	};
	}
   
   /* var colorButton=document.getElementById("changeColorBtn");	
   colorButton.onclick=function(event)
   {
   	changeColorInput();
   	}
   	
   //colorButton.onclick=changeColorInput();
   */
   
   //JQUERY kullanımları
   // document.ready -> bu sayfa tamamen yüklendikten sonra işlemleri yapar böylece scriptlerimizi <head> içine alabiliriz 
   $(document).ready(workWhenReady);
   
   
   
   function workWhenReady()
   {
	  var myelements=$(".sub-title");
   console.log("when it is ready: " + myelements.length);  	
   
   //direk buton id ile fonksiyonu eşitleyip çalıştırmak
      $("#changeColorBtn").click(function()
   {
   	alert("hey");
   	});
   	
   }
	
	//FONKSİYONU İÇERİ ALABİLİRİZ DİREK
	/*$(document).ready( function workWhenReady() 
   {
	  var myelements=$(".sub-title");
   console.log("when it is ready: " + myelements.length);  	
   }); */
	   
   var myelements=$(".sub-title");
   console.log(myelements.length);
   
