async function uploadDoc(input){
  if(!input.files[0]) return;
  const fd=new FormData(); fd.append("file",input.files[0]);
  const r=await fetch("/api/upload",{method:"POST",body:fd}); const d=await r.json();
  alert(d.message||d.error||"Upload complete"); if(r.ok) location.reload();
}
async function askAI(){
  const q=document.getElementById("question").value.trim(), box=document.getElementById("answer");
  if(!q) return; box.innerText="Searching knowledge base...";
  const fd=new FormData(); fd.append("question",q);
  const r=await fetch("/api/ask",{method:"POST",body:fd}); const d=await r.json();
  box.innerText=(d.answer||d.error)+"\n\nSources:\n"+(d.sources||[]).map((s,i)=>`[${i+1}] ${s.name} v${s.version}`).join("\n");
}
document.getElementById("question")?.addEventListener("keydown",e=>{if(e.key==="Enter")askAI()});
