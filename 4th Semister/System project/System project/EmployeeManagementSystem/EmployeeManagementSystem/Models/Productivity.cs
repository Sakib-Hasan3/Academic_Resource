using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace EmployeeManagementSystem.Models
{
    [Table("Productivity")]  // <-- CRITICAL: This must match exactly with the SQL table
    public class Productivity
    {
        [Key]
        public int ProductivityId { get; set; }

        [ForeignKey("Employee")]
        public int EmployeeId { get; set; }

        public string TaskDescription { get; set; }

        public DateTime TaskDate { get; set; }

        public int OutputQuantity { get; set; }

        public string Remarks { get; set; }

        public virtual Employee Employee { get; set; }
    }
}
