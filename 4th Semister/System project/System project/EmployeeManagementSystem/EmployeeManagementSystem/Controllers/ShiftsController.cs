using System;
using System.Collections.Generic;
using System.Data.Entity;
using System.Data.Entity.Validation;
using System.Linq;
using System.Net;
using System.Web.Mvc;
using EmployeeManagementSystem.Models;

namespace EmployeeManagementSystem.Controllers
{
    public class ShiftController : Controller
    {
        private EMSDbContext db = new EMSDbContext();

        // GET: /Shift/
        public ActionResult Index()
        {
            var shifts = db.Shifts.ToList();
            return View(shifts);
        }

        // GET: /Shift/Details/5
        public ActionResult Details(int? id)
        {
            if (id == null)
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);

            var shift = db.Shifts.Find(id);
            if (shift == null)
                return HttpNotFound();

            return View(shift);
        }

        // GET: /Shift/Create
        public ActionResult Create()
        {
            return View();
        }

        // POST: /Shift/Create
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Create(Shift shift)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    db.Shifts.Add(shift);
                    db.SaveChanges();
                    return RedirectToAction("Index");
                }
                catch (DbEntityValidationException dbEx)
                {
                    // Unwrap EF validation errors into ModelState
                    foreach (var validationErrors in dbEx.EntityValidationErrors)
                    {
                        foreach (var error in validationErrors.ValidationErrors)
                        {
                            ModelState.AddModelError(error.PropertyName, error.ErrorMessage);
                        }
                    }
                }
                catch (Exception ex)
                {
                    ModelState.AddModelError("", "Unable to save shift. " + ex.Message);
                }
            }

            // If we got this far, something failed; redisplay form
            return View(shift);
        }

        // GET: /Shift/Edit/5
        public ActionResult Edit(int? id)
        {
            if (id == null)
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);

            var shift = db.Shifts.Find(id);
            if (shift == null)
                return HttpNotFound();

            return View(shift);
        }

        // POST: /Shift/Edit/5
        [HttpPost]
        [ValidateAntiForgeryToken]
        public ActionResult Edit(Shift shift)
        {
            if (ModelState.IsValid)
            {
                try
                {
                    db.Entry(shift).State = EntityState.Modified;
                    db.SaveChanges();
                    return RedirectToAction("Index");
                }
                catch (DbEntityValidationException dbEx)
                {
                    foreach (var validationErrors in dbEx.EntityValidationErrors)
                    {
                        foreach (var error in validationErrors.ValidationErrors)
                        {
                            ModelState.AddModelError(error.PropertyName, error.ErrorMessage);
                        }
                    }
                }
                catch (Exception ex)
                {
                    ModelState.AddModelError("", "Unable to update shift. " + ex.Message);
                }
            }

            // Redisplay form on error
            return View(shift);
        }

        // GET: /Shift/Delete/5
        public ActionResult Delete(int? id)
        {
            if (id == null)
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);

            var shift = db.Shifts.Find(id);
            if (shift == null)
                return HttpNotFound();

            return View(shift);
        }

        // POST: /Shift/Delete/5
        [HttpPost, ActionName("Delete")]
        [ValidateAntiForgeryToken]
        public ActionResult DeleteConfirmed(int id)
        {
            try
            {
                var shift = db.Shifts.Find(id);
                db.Shifts.Remove(shift);
                db.SaveChanges();
                return RedirectToAction("Index");
            }
            catch (Exception ex)
            {
                ModelState.AddModelError("", "Unable to delete shift. " + ex.Message);
                // If deletion fails, redisplay the confirmation view
                var shift = db.Shifts.Find(id);
                return View("Delete", shift);
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
