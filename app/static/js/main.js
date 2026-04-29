const form=document.getElementById('chatForm');
if(form){
  const msgs=document.getElementById('msgs');
  const input=document.getElementById('message');
  const add=(text,role)=>{const d=document.createElement('div');d.className='msg '+role;d.textContent=text;msgs.appendChild(d);msgs.scrollTop=msgs.scrollHeight;};
  form.addEventListener('submit',async e=>{e.preventDefault();const text=input.value.trim();if(!text)return;add(text,'user');input.value='';try{const r=await fetch('/chat/send',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:text})});const data=await r.json();add(data.response||data.error||'Erro ao responder.','assistant');}catch(err){add('Falha de conexão. Tente novamente.','assistant');}});
}
