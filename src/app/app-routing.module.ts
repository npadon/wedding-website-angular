import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { TravelComponent } from './travel/travel.component';
import { RsvpComponent } from './rsvp/rsvp.component'
import { RegistryComponent } from './registry/registry.component'
import { ContactComponent } from './contact/contact.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'travel', component: TravelComponent },
  { path: 'rsvp', component: RsvpComponent },
  { path: 'registry', component: RegistryComponent },
  { path: 'contact', component: ContactComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
