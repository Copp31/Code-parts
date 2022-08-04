// ********************************************** Constantes et setting de base

const express = require('express')
const app = express()
const PORT = 4200
const expressLayouts = require('express-ejs-layouts')
const mongoose = require("mongoose")

app.use(function (req, res, next) {
    res.setHeader("Access-Control-Allow-Origin", "*");
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    res.setHeader('Access-Control-Allow-Credentials', true);
    next();
});
app.use(express.json());


// ********************************************** Statics files

const emplacementLocal = 'C:/Users/coppe/OneDrive/Desktop/github/AAAAA_2/AAAAA'
const emplacementStyle = `${emplacementLocal}/style/`
const emplacementJS = `${emplacementLocal}/interactions/`

app.use('/style', express.static(emplacementStyle))
app.use('/interactions', express.static(emplacementJS))

app.listen(PORT, () => {
    console.log(`Serveur en ecoute sur le PORT ${PORT}... `)
  })

app.use(expressLayouts)
app.set('layout', './layouts/full-width')
app.set('view engine', 'ejs')


// ********************************************** Mongoose 

let db = 'mongodb://localhost/mongoose'
mongoose
    .connect(db, {useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log("Connecté à la BD Mongo..."))
    .catch(error => console.log("Echec de connexion à la BD Mongo...", error));

const userDataSchema = new mongoose.Schema({
    nom: String,
    prenom: String,
    entreprise: String,
    telephone: String,
    mobile: String,
    email: String,
    adresse: String
});

const Contacts = mongoose.model('contact', userDataSchema, 'Contacts');



//  ************************************************************************* Roots

app.get('/', (req, res) => {
    res.render('repertoire', {titre: 'Répertoire'})
})

app.get('/add', (req, res) => {
    res.render('add_contact', {titre: 'AjouterContact'})
})



// ******* Accès au répertoire complet des enregistrements de la BD

app.get('/personnes', async (req, res) => {
    console.log("Route GET /personnes");
    try { 
        let result = await Contacts.find().exec();
        res.send(result);
    } 
    catch (error) {
        res.status(500).send(error);
    }
});


// ******* Accès enregistrement en particulier dans la BD

app.get("/personne/:id", async (req, res) => {
    let texte = `Contact ID récupéré: ${req.params.id}`
    console.log(texte);
    try {
        let contact = await Contacts.findById(req.params.id).exec();
        res.send(contact);
    } 
    catch (error) {
        res.status(500).send(error);
    }
});

// *******  Ajouter un enregistrement

app.post('/personne', async (request, response) => {
    console.log("Route POST /personne");
    console.log(request.body);
    try {
        let person = new Contacts(request.body);
        let result = await person.save();
        response.send(result);

    }
    catch (error) {
        response.status(500).send(error);
    }
});

// ******* Effacer un enregistrement 

app.delete("/personne/:id", async (req, res) => {
    try {
        let result = await Contacts.deleteOne({ _id: req.params.id }).exec();
        res.send(result);
    } 
    catch (error) {
        res.status(500).send(error);
    }
});



// ******* Mettre a jour enregistrement

app.put("/personne/:id", async (req, res) => {
    console.log("Route PUT /personne/:id");
    console.log(req.body);
    try {
        let person = await Contacts.findById(req.params.id).exec();
        person.set(req.body);
        let result = await person.save();
        res.send(result);
    } 
    catch (error) {
        res.status(500).send(error);
    }
});
