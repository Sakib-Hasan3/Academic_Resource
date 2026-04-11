using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web.Mvc;
using EmployeeManagementSystem.Models;

namespace EmployeeManagementSystem.Controllers
{
    public class LeaveController : Controller
    {
        private EMSDbContext db = new EMSDbContext();

        public ActionResult Index() =>
            View(db.Leaves.Include(l => l.Employee).ToList());

        public ActionResult Details(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            Leave leave = db.Leaves.Find(id);
            if (leave == null) return HttpNotFound();
            return View(leave);
        }

        public ActionResult Create()
        {
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName");
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(Leave leave)
        {
            if (ModelState.IsValid)
            {
                db.Leaves.Add(leave);
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", leave.EmployeeId);
            return View(leave);
        }

        public ActionResult Edit(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            Leave leave = db.Leaves.Find(id);
            if (leave == null) return HttpNotFound();
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", leave.EmployeeId);
            return View(leave);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(Leave leave)
        {
            if (ModelState.IsValid)
            {
                db.Entry(leave).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", leave.EmployeeId);
            return View(leave);
        }

        public ActionResult Delete(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            Leave leave = db.Leaves.Find(id);
            if (leave == null) return HttpNotFound();
            return View(leave);
        }

        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Leave leave = db.Leaves.Find(id);
            db.Leaves.Remove(leave);
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
