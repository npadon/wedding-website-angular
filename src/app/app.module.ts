import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { AppNavComponent } from './app-nav/app-nav.component';
import { RsvpComponent } from './rsvp/rsvp.component';
import { HomeComponent } from './home/home.component';
import { TravelComponent } from './travel/travel.component';
import { RegistryComponent } from './registry/registry.component';
import { HttpClientModule } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { RsvpFormComponent } from './rsvp-form/rsvp-form.component';
import { ContactComponent } from './contact/contact.component';

@NgModule({
  declarations: [
    AppComponent,
    AppNavComponent,
    RsvpComponent,
    HomeComponent,
    TravelComponent,
    RegistryComponent,
    RsvpFormComponent,
    ContactComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
