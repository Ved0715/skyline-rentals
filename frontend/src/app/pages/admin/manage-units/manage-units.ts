import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../../services/api.service';

@Component({
  selector: 'app-manage-units',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './manage-units.html'
})
export class ManageUnitsComponent implements OnInit {
  units: any[] = [];
  towers: any[] = [];
  loading = false;
  showModal = false;
  unitForm: FormGroup;

  constructor(
    private apiService: ApiService,
    private fb: FormBuilder
  ) {
    this.unitForm = this.fb.group({
      tower_id: ['', Validators.required],
      unit_number: ['', Validators.required],
      floor: ['', [Validators.required, Validators.min(1)]],
      bedrooms: ['', [Validators.required, Validators.min(1)]],
      bathrooms: ['', [Validators.required, Validators.min(1)]],
      area_sqft: ['', [Validators.required, Validators.min(1)]],
      monthly_rent: ['', [Validators.required, Validators.min(1)]],
      description: ['']
    });
  }

  ngOnInit() {
    this.loadUnits();
    this.loadTowers();
  }

  loadUnits() {
    this.loading = true;
    this.apiService.getUnits().subscribe({
      next: (data) => {
        this.units = data;
        this.loading = false;
      },
      error: () => this.loading = false
    });
  }

  loadTowers() {
    this.apiService.getTowers().subscribe({
      next: (data) => this.towers = data
    });
  }

  openModal() {
    this.showModal = true;
    this.unitForm.reset();
  }

  closeModal() {
    this.showModal = false;
  }

  createUnit() {
    if (this.unitForm.valid) {
      this.apiService.createUnit(this.unitForm.value).subscribe({
        next: () => {
          alert('Unit created successfully!');
          this.closeModal();
          this.loadUnits();
        },
        error: (err) => alert(err.error?.message || 'Failed to create unit')
      });
    }
  }
}
