using System.Data.Entity;

namespace EmployeeManagementSystem.Models
{
    public class EMSDbContext : DbContext
    {
        public EMSDbContext() : base("name=EmployeeDBConnection") { }

        public DbSet<Employee> Employees { get; set; }
        public DbSet<Shift> Shifts { get; set; }
        public DbSet<Attendance> Attendances { get; set; }
        public DbSet<Leave> Leaves { get; set; }
        public DbSet<Payroll> Payrolls { get; set; }
        public DbSet<Productivity> Productivities { get; set; }
    }
}
