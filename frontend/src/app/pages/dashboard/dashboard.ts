import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.html'
})
export class DashboardComponent implements OnInit {
  units: any[] = [];
  myBookings: any[] = [];
  loading = false;
  user: any;
  activeTab: 'apartments' | 'mybookings' | 'profile' = 'apartments';
  selectedUnit: any = null;

  constructor(
    private apiService: ApiService,
    private authService: AuthService
  ) {
    this.user = this.authService.getCurrentUser();
  }

  ngOnInit() {
    this.loadData();
  }

  loadData() {
    this.loading = true;
    
    this.apiService.getUnits('available').subscribe({
      next: (data) => {
        this.units = data;
        this.loading = false;
      },
      error: () => this.loading = false
    });

    this.apiService.getMyBookings().subscribe({
      next: (data) => this.myBookings = data
    });
  }

  bookUnit(unitId: string) {
    if (confirm('Request booking for this apartment?')) {
      const today = new Date().toISOString().split('T')[0];
      this.apiService.requestBooking({ 
        unit_id: unitId, 
        preferred_move_in: today 
      }).subscribe({
        next: () => {
          alert('Booking requested successfully!');
          this.closeModal(); // Close the modal
          this.activeTab = 'mybookings'; // Switch to bookings tab
          this.loadData();
        },
        error: (err) => {
          console.error('Booking error:', err);
          alert(err.error?.message || 'Booking failed. Please try again.');
        }
      });
    }
  }

  logout() {
    this.authService.logout();
  }

  viewDetails(unit: any) {
    this.selectedUnit = unit;
  }

  closeModal() {
    this.selectedUnit = null;
  }
}