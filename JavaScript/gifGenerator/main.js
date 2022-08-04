const baseUrl="https://api.giphy.com/v1/"

const api_key='lQ72kikjvn15iF2TperWQ8b1DdXMr12H'
const searchBar= document.getElementById("searchBar")
const searchButton = document.getElementById("search")
const translateButton = document.getElementById("translate")
const displayContainer=document.getElementById("displayContainer")


searchButton.addEventListener("click",()=>{
    displayContainer.innerHTML=""
    const request = searchBar.value
    getGifsResults(request)
})
translateButton.addEventListener("click",()=>{
    displayContainer.innerHTML=""
    const request = searchBar.value
    getStickersResults(request)
})

const getGifsResults = async (searchRequest)=>{
    try{
    const results = await fetch(`${baseUrl}gifs/search?q=${searchRequest}&api_key=${api_key}&limit=5`,{mode:"cors"})
    const dataResults = await results.json()
     //console.log(dataResults) // POUR DEBUGGER
    dataResults.data.forEach(element=>{
        const img = document.createElement("img")
        img.src=element.images["original"].url
        displayContainer.appendChild(img)
    })
    if (dataResults.data.length===0) displayContainer.textContent="Aucun résultat"
} catch(error){
    console.log(error)
}
}
const getStickersResults = async (searchRequest) =>{ 
    try {
    const res = await fetch(`${baseUrl}stickers/search?q=${searchRequest}&api_key=${api_key}&limit=5`,{mode:"cors"})
    const datares = await res.json()
     //console.log(dataResults) // POUR DEBUGGER
     datares.data.forEach(element=>{
        const img = document.createElement("img")
        img.src=element.images["original"].url
        displayContainer.appendChild(img)
    })
    if (datares.data.length===0) displayContainer.textContent="Aucun résultat"
} catch(error){
    console.log(error)
    }


        
}

   
