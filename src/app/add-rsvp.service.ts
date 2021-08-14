import { Injectable } from '@angular/core';
import { HttpClient, HttpResponse } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { RSVP } from './models/rsvp';
import { RSVPResponse } from './models/rsvp_response';

@Injectable({
  providedIn: 'root',
})
export class AddRsvpService {
  baseUrl = environment.baseUrl;
  constructor(protected http: HttpClient) {}
  getRSVP(): Observable<String[]> {
    return this.http.get<String[]>(`${this.baseUrl}v1/rsvp`);
  }

  postRSVP(rsvp: RSVP): Observable<RSVPResponse> {
    return this.http.post<RSVPResponse>(`${this.baseUrl}v1/rsvp`, rsvp);
  }
}
