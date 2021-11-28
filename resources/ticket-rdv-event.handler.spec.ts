/* eslint-disable @typescript-eslint/no-non-null-assertion */
import { ConfigService } from '@devon4node/config';
import { Test, TestingModule } from '@nestjs/testing';
import { IEvent } from 'smt-shared-lib/lib/shared/types/event.interface';
import Config from '../../../config/test';
import { CoreModule } from '../../core/core.module';
import { Ticket } from '../../ticket/model/schemas/events/ticket.schema';
import { TicketRepository } from '../../ticket/repositories/ticket.repository';
import { RDVModule } from '../rdv.module';
import { RDVRepository } from '../repositories/rdv.repository';
import { TicketRdvEventHandler } from './ticket-rdv-event.handler';

describe('TicketRdvEventHandler', () => {
  let module: TestingModule;
  let handler: TicketRdvEventHandler;
  let repository: TicketRepository;

  const input: IEvent<Ticket> = {
    payload: {
      after: {
        TICKETID: '1853106',
        CLASS: 'SR',
        DESCRIPTION: 'test01',
        STATUS: 'BROUILLON',
        STATUSDATE: new Date(1635206290000),
        REPORTDATE: new Date(1635206290000),
        ISGLOBAL: '0',
        RELATEDTOGLOBAL: '0',
        SITEVISIT: '0',
        INHERITSTATUS: '1',
        ISKNOWNERROR: '0',
        SITEID: 'MATERIEL',
        ORGID: 'SNCF',
        CHANGEDATE: new Date(1635206290000),
        CHANGEBY: 'PCA01',
        HISTORYFLAG: '0',
        TEMPLATE: '0',
        HASACTIVITY: '0',
        ACTLABHRS: '0',
        ACTLABCOST: '0.00',
        ASSETSITEID: 'MATERIEL',
        ASSETNUM: '6841',
        LOCATION: '26',
        TICKETUID: '6181725',
        ASSETORGID: 'SNCF',
        LANGCODE: 'FR',
        HASLD: '0',
        CREATEWOMULTI: 'MULTI',
        SELFSERVSOLACCESS: '0',
        HASSOLUTION: '0',
        PLUSAEVENTTYPE: 'OPERATIONAL',
        PLUSAADMINEVENT: '0',
        PLUSAACCTMAINTFLAG: '0',
        PLUSAMANAGEWITHWRFL: '0',
        PLUSAREMOTESITERESCUE: '0',
        PLUSAUNCONTFAILURE: '0',
        PLUSAVIGVMAX: '0.00',
        PLUSAPILOTPROC: '0',
        PLUSAETOPS: '0',
        PLUSAFALSEALARM: '0',
        OSM_CAUSEAPPRO: '0',
        OSM_AFA: '0',
        OSM_ALAP: '0',
        OSM_ANOTIFIER: '0',
        OSM_CREATEUR: 'PCA01',
        OSM_DATDEBRDV: new Date(1635206400000),
        OSM_DATECREATION: new Date(1635206290000),
        OSM_DATFINRDV: new Date(1635207300000),
        OSM_IDSERIE: 'VUAUTREEVA-ATEO',
        OSM_MRSTATGARANT: 'Non',
        OSM_NUM_IDENT_EU: '508721821314',
        OSM_NUM_IMMAT_EF: '872182131',
        OSM_RECIDIVE: '0',
        OSM_SITEREAL: 'TLA',
        OSM_STF: 'SBF',
        OSM_TYPE_SR: 'RDV',
        ROWSTAMP: '21572118438',
        OSM_IMPERATIF: '0',
        OSM_LIEUREALID: '469',
        OSM_LIEU_REAL: 'TLA',
        OSM_MAINT_DELOCALISEE: '0',
        OSM_REF_LIEU_REAL: 'MA0077',
        OSM_ARCHIVE: '0',
        OSM_WASMODIFUTIL: '1',
      },
      source: {
        version: '1.7.0.Final',
        connector: 'oracle',
        name: '10.148.6.148',
        ts_ms: 1635206408000,
        snapshot: 'false',
        db: 'OSMOD36',
        schema: 'MAXIMO',
        table: 'TICKET',
        txId: '001200060010ae2b',
        scn: 10136604211887,
        commit_scn: '10136604212062',
      },
      op: 'c',
      ts_ms: 1635199234156,
    },
  };

  const expectedResult = expect.objectContaining({
    debutRDV: new Date('2021-10-26T00:00:00.000Z'),
    estFictif: false,
    estImperatif: false,
    evenementsMaintenance: [],
    finRDV: new Date('2021-10-26T00:15:00.000Z'),
    flotte: '26',
    idGMAO: '1853106',
    idSerie: 'VUAUTREEVA-ATEO',
    invariantMR: 'test',
    libelleRDV: 'test01',
    numeroActif: '6841',
    siteReal: 'TLA',
    statutRDV: 'BROUILLON',
    stf: 'SBF',
  });

  beforeAll(async () => {
    module = await Test.createTestingModule({
      imports: [RDVModule, CoreModule],
    })
      .overrideProvider(ConfigService)
      .useValue({ values: Config })
      .overrideProvider('KAFKA_CLIENT')
      .useValue(jest.fn())
      .compile();

    handler = module.get(TicketRdvEventHandler);
    repository = module.get(RDVRepository);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  afterAll(async () => {
    await module.close();
  });

  it('should be defined', () => {
    expect(handler).toBeDefined();
    input;
  });

  it('when receive a ticket event then create a RDV', async () => {
    await handler.handle(input);
    const result = (await repository.findByQuery({ idGMAO: input.payload.after.TICKETID }))[0];
    expect(result).toEqual(expectedResult);
  });
});
