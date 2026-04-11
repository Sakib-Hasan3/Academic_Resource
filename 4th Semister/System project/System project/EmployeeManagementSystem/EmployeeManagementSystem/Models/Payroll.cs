using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace EmployeeManagementSystem.Models
{
    public class Payroll
    {
        [Key]
        public int PayrollId { get; set; }

        [ForeignKey("Employee")]
        public int EmployeeId { get; set; }

        public string Month { get; set; }

        public decimal BasicSalary { get; set; }

        public decimal AttendanceBonus { get; set; }

        public decimal Deductions { get; set; }

        [NotMapped]
        public decimal NetSalary => BasicSalary + AttendanceBonus - Deductions;

        public DateTime GeneratedDate { get; set; }

        public virtual Employee Employee { get; set; }
    }
}
