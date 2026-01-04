import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:5001/api';

  constructor(private http: HttpClient) {}

  // Public Endpoints
  getUnits(status?: string): Observable<any> {
    let params = new HttpParams();
    if (status) params = params.set('status', status);
    return this.http.get(`${this.apiUrl}/units`, { params });
  }

  getTowers(): Observable<any> {
    return this.http.get(`${this.apiUrl}/towers`);
  }

  // Protected Endpoints (Token auto-injected by Interceptor)
  getMyBookings(): Observable<any> {
    return this.http.get(`${this.apiUrl}/bookings/my`);
  }

  requestBooking(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/bookings/`, data);
  }

  // Admin Endpoints
  getAdminStats(): Observable<any> {
    return this.http.get(`${this.apiUrl}/admin/dashboard/stats`);
  }

  getAdminBookings(): Observable<any> {
    return this.http.get(`${this.apiUrl}/bookings`);
  }

  updateBookingStatus(id: string, status: string): Observable<any> {
    return this.http.put(`${this.apiUrl}/bookings/${id}/status`, { status });
  }

  createUnit(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/units`, data);
  }
}