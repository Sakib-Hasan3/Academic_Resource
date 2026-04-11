using System;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web.Mvc;
using EmployeeManagementSystem.Models;

namespace EmployeeManagementSystem.Controllers
{
    public class AttendanceController : Controller
    {
        private EMSDbContext db = new EMSDbContext();

        // GET: /Attendance/
        public ActionResult Index()
        {
            var list = db.Attendances
                         .Include(a => a.Employee)
                         .ToList();
            return View(list);
        }

        // GET: /Attendance/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);

            var attendance = db.Attendances
                               .Include(a => a.Employee)
                               .FirstOrDefault(a => a.AttendanceId == id);
            if (attendance == null)
                return HttpNotFound();

            return View(attendance);
        }

        // GET: /Attendance/Create
        public ActionResult Create()
        {
            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName");
            return View();
        }

        // POST: /Attendance/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(Attendance attendance)
        {
            // Check model validation
            if (!ModelState.IsValid)
            {
                ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", attendance.EmployeeId);
                return View(attendance);
            }

            // Verify foreign key
            if (!db.Employees.Any(e => e.EmployeeId == attendance.EmployeeId))
            {
                ModelState.AddModelError("EmployeeId", "Selected employee does not exist.");
                ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", attendance.EmployeeId);
                return View(attendance);
            }

            try
            {
                db.Attendances.Add(attendance);
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("", "Error saving attendance: " + (ex.InnerException?.Message ?? ex.Message));
                ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", attendance.EmployeeId);
                return View(attendance);
            }
        }

        // GET: /Attendance/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);

            var attendance = db.Attendances.Find(id);
            if (attendance == null)
                return HttpNotFound();

            ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", attendance.EmployeeId);
            return View(attendance);
        }

        // POST: /Attendance/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(Attendance attendance)
        {
            if (!ModelState.IsValid)
            {
                ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", attendance.EmployeeId);
                return View(attendance);
            }

            try
            {
                db.Entry(attendance).State = EntityState.Modified;
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("", "Error updating attendance: " + (ex.InnerException?.Message ?? ex.Message));
                ViewBag.EmployeeId = new SelectList(db.Employees, "EmployeeId", "FullName", attendance.EmployeeId);
                return View(attendance);
            }
        }

        // GET: /Attendance/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);

            var attendance = db.Attendances.Find(id);
            if (attendance == null)
                return HttpNotFound();

            return View(attendance);
        }

        // POST: /Attendance/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            try
            {
                var attendance = db.Attendances.Find(id);
                db.Attendances.Remove(attendance);
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("", "Error deleting attendance: " + (ex.InnerException?.Message ?? ex.Message));
                var attendance = db.Attendances.Find(id);
                return View("Delete", attendance);
            }
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
                db.Dispose();
            base.Dispose(disposing);
        }
    }
}
