using System;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace EmployeeManagementSystem.Models
{
    public class Leave
    {
        [Key]
        public int LeaveId { get; set; }

        [ForeignKey("Employee")]
        public int EmployeeId { get; set; }

        public DateTime LeaveDate { get; set; }

        public string Reason { get; set; }

        public string Status { get; set; } // "Pending", "Approved", "Rejected"

        public virtual Employee Employee { get; set; }
    }
}
