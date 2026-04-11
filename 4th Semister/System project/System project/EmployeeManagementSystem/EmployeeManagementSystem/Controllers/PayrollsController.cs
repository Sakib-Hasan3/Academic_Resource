using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web.Mvc;
using EmployeeManagementSystem.Models;

namespace EmployeeManagementSystem.Controllers
{
    public class PayrollController : Controller
    {
        private EMSDbContext db = new EMSDbContext();

        public ActionResult Index() =>
            View(db.Payrolls.Include(p => p.Employee).ToList());

        public ActionResult Details(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            Payroll payroll = db.Payrolls.Find(id);
            if (payroll == null) return HttpNotFound();
            return View(payroll);
        }

        public ActionResult Create()
        {
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName");
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(Payroll payroll)
        {
            if (ModelState.IsValid)
            {
                db.Payrolls.Add(payroll);
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", payroll.EmployeeId);
            return View(payroll);
        }

        public ActionResult Edit(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);

            Payroll payroll = db.Payrolls.Find(id);
            if (payroll == null) return HttpNotFound();
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", payroll.EmployeeId);
            return View(payroll);
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(Payroll payroll)
        {
            if (ModelState.IsValid)
            {
                db.Entry(payroll).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", payroll.EmployeeId);
            return View(payroll);
        }

        public ActionResult Delete(int? id)
        {
            if (id == null) return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            Payroll payroll = db.Payrolls.Find(id);
            if (payroll == null) return HttpNotFound();
            return View(payroll);
        }

        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            Payroll payroll = db.Payrolls.Find(id);
            db.Payrolls.Remove(payroll);
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
