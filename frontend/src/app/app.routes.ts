import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home';
import { LoginComponent } from './pages/login/login';
import { RegisterComponent } from './pages/register/register';
import { DashboardComponent } from './pages/dashboard/dashboard';
import { LayoutComponent } from './pages/admin/layout/layout';
import { DashboardComponent as AdminDashboardComponent } from './pages/admin/dashboard/dashboard';
import { ManageUnitsComponent } from './pages/admin/manage-units/manage-units';
import { ManageBookingsComponent } from './pages/admin/manage-bookings/manage-bookings';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'dashboard', component: DashboardComponent },
  { 
    path: 'admin', 
    component: LayoutComponent,
    children: [
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
      { path: 'dashboard', component: AdminDashboardComponent },
      { path: 'units', component: ManageUnitsComponent },
      { path: 'bookings', component: ManageBookingsComponent }
    ]
  },
  { path: '**', redirectTo: '' }
];