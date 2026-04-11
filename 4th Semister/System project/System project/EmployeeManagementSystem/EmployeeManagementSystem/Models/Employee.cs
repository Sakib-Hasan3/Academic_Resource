using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace EmployeeManagementSystem.Models
{
    public class Employee
    {
        [Key]
        public int EmployeeId { get; set; }

        [Required]
        public string FullName { get; set; }

        public string Designation { get; set; }

        public DateTime DateOfJoining { get; set; }

        public decimal Salary { get; set; }

        public string ContactNumber { get; set; }

        public string Email { get; set; }

        public string Address { get; set; }

        public int? ShiftId { get; set; }

        [ForeignKey("ShiftId")]
        public virtual Shift Shift { get; set; }
    }
}
