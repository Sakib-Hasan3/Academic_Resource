using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web.Mvc;
using EmployeeManagementSystem.Models;

namespace EmployeeManagementSystem.Controllers
{
    public class ProductivityController : Controller
    {
        private EMSDbContext db = new EMSDbContext();

        public ActionResult Index()
        {
            var list = db.Productivities.ToList(); // no include
            return View(list);
        }


        public ActionResult Details(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            Productivity productivity = db.Productivities.Find(id);
            if (productivity == null) return HttpNotFound();
            return View(productivity);
        }

        public ActionResult Create()
        {
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName");
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(Productivity productivity)
        {
            if (ModelState.IsValid)
            {
                db.Productivities.Add(productivity);
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", productivity.EmployeeId);
            return View(productivity);
        }

        public ActionResult Edit(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            Productivity productivity = db.Productivities.Find(id);
            if (productivity == null) return HttpNotFound();
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", productivity.EmployeeId);
            return View(productivity);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(Productivity productivity)
        {
            if (ModelState.IsValid)
            {
                db.Entry(productivity).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", productivity.EmployeeId);
            return View(productivity);
        }

        public ActionResult Delete(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            Productivity productivity = db.Productivities.Find(id);
            if (productivity == null) return HttpNotFound();
            return View(productivity);
        }

        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Productivity productivity = db.Productivities.Find(id);
            db.Productivities.Remove(productivity);
            db.SaveChanges();
            return RedirectToAction("Index");
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing) db.Dispose();
            base.Dispose(disposing);
        }
    }
}
