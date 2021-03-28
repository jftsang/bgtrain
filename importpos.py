import logging, os, glob
import gnubg.common as gc

logger = logging.getLogger(__name__)
ROOT_DIR = os.path.dirname(__file__)

with gc.get_conn() as conn:
    for path in glob.glob(os.path.join(ROOT_DIR, 'dump', '*.csv')):
        print('Processing', path, '...')
        with open(path, 'rb') as inf:
            for line in inf:
                posmatchid, decisiontype, move, equity, version, ply = line.split(';')
                sql = '''
                    insert ignore
                    into posmatchids
                    (posmatchid, decisiontype, version, createddate)
                    values
                    (%s, %s, %s, current_timestamp)
                '''
                conn.execute(sql, [posmatchid, decisiontype, version])

                sql = '''
                    replace
                    into
                    analyses
                    (posmatchid, move, equity, ply)
                    values
                    (%s, %s, %s, %s)
                '''
                conn.execute(sql, [posmatchid, move, equity, ply if ply != 'None' else None])
        conn.commit()
        os.rename(path, path + '.processed')
        print('Done processing', path)
        print()


            

