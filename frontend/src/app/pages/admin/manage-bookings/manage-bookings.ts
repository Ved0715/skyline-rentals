import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../../services/api.service';

@Component({
  selector: 'app-manage-bookings',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './manage-bookings.html'
})
export class ManageBookingsComponent implements OnInit {
  bookings: any[] = [];
  loading = false;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.loadBookings();
  }

  loadBookings() {
    this.loading = true;
    this.apiService.getAdminBookings().subscribe({
      next: (data) => {
        this.bookings = data;
        this.loading = false;
      },
      error: () => this.loading = false
    });
  }

  updateStatus(bookingId: string, status: string) {
    const action = status === 'approved' ? 'approve' : 'decline';
    if (confirm(`Are you sure you want to ${action} this booking?`)) {
      this.apiService.updateBookingStatus(bookingId, status).subscribe({
        next: () => {
          alert(`Booking ${status} successfully!`);
          this.loadBookings();
        },
        error: (err) => alert(err.error?.message || 'Failed to update booking')
      });
    }
  }
}
