using Microsoft.AspNetCore.Mvc;
using MongoDB.Driver;
using MongoDB.Bson;
using System.Collections.Generic;

namespace MeuProjeto.Controllers
{
    public class PessoasController : Controller
    {
        private readonly IMongoCollection<Pessoa> _pessoas;

        public PessoasController()
        {
            string connectionString = "mongodb+srv://usuario:senha@n703.dfo9g.mongodb.net/?retryWrites=true&w=majority&appName=N703";
            var client = new MongoClient(connectionString);
            var database = client.GetDatabase("N703-WEB-SERVICE");
            _pessoas = database.GetCollection<Pessoa>("Pessoas");
        }

        public IActionResult Index()
        {
            var pessoas = _pessoas.Find(new BsonDocument()).ToList();
            return View(pessoas);
        }

        public IActionResult Adicionar()
        {
            return View();
        }

        [HttpPost]
        public IActionResult Adicionar(Pessoa pessoa)
        {
            _pessoas.InsertOne(pessoa);
            return RedirectToAction("Index");
        }

        public IActionResult Editar(string id)
        {
            var pessoa = _pessoas.Find(p => p.Id == id).FirstOrDefault();
            return View(pessoa);
        }

        [HttpPost]
        public IActionResult Editar(string id, Pessoa pessoa)
        {
            var filter = Builders<Pessoa>.Filter.Eq("_id", new ObjectId(id));
            var update = Builders<Pessoa>.Update
                .Set("Nome", pessoa.Nome)
                .Set("Idade", pessoa.Idade)
                .Set("Contato", pessoa.Contato);

            _pessoas.UpdateOne(filter, update);
            return RedirectToAction("Index");
        }

        public IActionResult Deletar(string id)
        {
            _pessoas.DeleteOne(p => p.Id == id);
            return RedirectToAction("Index");
        }
    }

    public class Pessoa
    {
        public string Id { get; set; }
        public string Nome { get; set; }
        public int Idade { get; set; }
        public string Contato { get; set; }
    }
}

