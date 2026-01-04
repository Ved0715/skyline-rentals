import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './home.html'
})
export class HomeComponent implements OnInit {
  units: any[] = [];
  loading = true;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.apiService.getUnits('available').subscribe({
      next: (data) => {
        this.units = data;
        this.loading = false;
      },
      error: () => this.loading = false
    });
  }

  scrollToFeatured() {
    document.getElementById('featured-units')?.scrollIntoView({ behavior: 'smooth' });
  }
}