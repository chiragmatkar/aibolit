import java.util.ArrayList;

class Test extends SuperClass {
    @Override
    public void foo() {
        try {
			new Thread() {
				@Override
				public void run() {
					ArrayList<Boolean> list = new ArrayList<Boolean>();
					for (int i = 0; i < 10; i++)
						for (int j = 0; j < 10; j++)
							list.add(Boolean.FALSE);
					try {
						super.method1();
					}
					catch (IOException e) {
						throw e;
					}
				}
			}.start();
		}
		catch (Exception e){
			throw e;
		}
    }
} 